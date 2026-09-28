/**
 * Model Context Protocol (MCP) TypeScript Client Bridge
 */

export interface MCPTool {
  name: string;
  description: string;
  inputSchema: Record<string, unknown>;
}

export class MCPClientBridge {
  private gatewayUrl: string;

  constructor(gatewayUrl: string = "http://localhost:8088/mcp") {
    this.gatewayUrl = gatewayUrl;
  }

  public async listTools(): Promise<MCPTool[]> {
    console.log(`Querying available MCP tools from ${this.gatewayUrl}...`);
    return [
      {
        name: "query_postgres",
        description: "Executes read-only queries",
        inputSchema: { type: "object" }
      },
      {
        name: "trigger_github_action",
        description: "Dispatches workflow runs",
        inputSchema: { type: "object" }
      }
    ];
  }
}
