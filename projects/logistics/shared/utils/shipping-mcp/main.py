"""shipping-mcp — placeholder MCP server exposing shipment-tracking tools.

Demo only: returns canned data, calls no external services.
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("shipping-mcp")


@mcp.tool()
def track_container(container_id: str) -> dict:
    """Return the current status of a container."""
    return {
        "container_id": container_id,
        "status": "IN_TRANSIT",
        "last_port": "PORT-A",
        "next_port": "PORT-B",
        "eta": "2026-10-05T12:00:00Z",
    }


@mcp.tool()
def list_bookings(customer_ref: str) -> list[dict]:
    """List bookings for a customer reference."""
    return [
        {"booking_id": "BKG-0001", "customer_ref": customer_ref, "containers": 2},
        {"booking_id": "BKG-0002", "customer_ref": customer_ref, "containers": 1},
    ]


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
