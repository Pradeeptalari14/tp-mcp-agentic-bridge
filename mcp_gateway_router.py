#!/usr/bin/env python3
"""
Universal MCP Gateway Router
Implements Model Context Protocol (MCP) JSON-RPC 2.0 endpoint with RBAC tool verification.
"""

import sys
import json
import logging
from typing import Dict, List, Any
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("MCPGateway")

class ToolDefinition(BaseModel):
    name: str
    description: str
    inputSchema: Dict[str, Any]
    requiredRoles: List[str] = Field(default_factory=lambda: ["agent"])

class MCPRequest(BaseModel):
    jsonrpc: str = "2.0"
    id: str
    method: str
    params: Dict[str, Any] = Field(default_factory=dict)

class MCPGatewayRouter:
    def __init__(self):
        self.tools: Dict[str, ToolDefinition] = {}
        self._register_default_tools()
        logger.info("Initialized Universal MCP Gateway Router")

    def _register_default_tools(self):
        self.register_tool(ToolDefinition(
            name="query_postgres",
            description="Executes a safe read-only SQL query against the warehouse database.",
            inputSchema={"type": "object", "properties": {"sql": {"type": "string"}}, "required": ["sql"]},
            requiredRoles=["analyst", "sre"]
        ))
        self.register_tool(ToolDefinition(
            name="trigger_github_action",
            description="Dispatches a workflow run in the target repository.",
            inputSchema={"type": "object", "properties": {"repo": {"type": "string"}, "workflow": {"type": "string"}}, "required": ["repo", "workflow"]},
            requiredRoles=["admin", "sre"]
        ))
        self.register_tool(ToolDefinition(
            name="kubectl_get_pods",
            description="Retrieves active pods within a designated Kubernetes namespace.",
            inputSchema={"type": "object", "properties": {"namespace": {"type": "string"}}, "required": ["namespace"]},
            requiredRoles=["sre"]
        ))

    def register_tool(self, tool: ToolDefinition):
        self.tools[tool.name] = tool
        logger.info(f"Registered MCP tool: {tool.name}")

    def handle_request(self, request: MCPRequest, user_role: str = "sre") -> Dict[str, Any]:
        if request.method == "tools/list":
            authorized_tools = [
                {"name": t.name, "description": t.description, "inputSchema": t.inputSchema}
                for t in self.tools.values()
                if user_role in t.requiredRoles
            ]
            return {"jsonrpc": "2.0", "id": request.id, "result": {"tools": authorized_tools}}
        
        elif request.method == "tools/call":
            tool_name = request.params.get("name")
            if tool_name not in self.tools:
                return {"jsonrpc": "2.0", "id": request.id, "error": {"code": -32601, "message": "Method not found"}}
            tool = self.tools[tool_name]
            if user_role not in tool.requiredRoles:
                return {"jsonrpc": "2.0", "id": request.id, "error": {"code": -32000, "message": "Access Denied: Insufficient RBAC role"}}
            
            # Execute tool logic mock
            return {
                "jsonrpc": "2.0",
                "id": request.id,
                "result": {
                    "content": [{"type": "text", "text": f"Successfully executed tool '{tool_name}' with role '{user_role}'"}],
                    "isError": False
                }
            }
        return {"jsonrpc": "2.0", "id": request.id, "error": {"code": -32600, "message": "Invalid Request"}}

if __name__ == "__main__":
    router = MCPGatewayRouter()
    req = MCPRequest(id="msg-1", method="tools/list")
    resp = router.handle_request(req, "sre")
    print(json.dumps(resp, indent=2))
