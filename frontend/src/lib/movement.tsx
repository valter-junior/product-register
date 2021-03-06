const baseUrl = "http://localhost:8000";

export const MovementProduct = async (body) => {
    const res = await fetch(`${baseUrl}/product/movement`, {
        method: "GET",
        headers: { "Content-Type": "application/json" },
        // We convert the React state to JSON and send it as the POST body
        body: JSON.stringify(body)

    });
    return res.json();
}