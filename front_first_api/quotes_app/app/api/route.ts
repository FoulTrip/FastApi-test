import { NextApiRequest, NextApiResponse } from "next";
import { NextResponse } from "next/server";

export async function GET() {
  const res = await fetch("http://127.0.0.1:8000/authors", {
    headers: {
      "Content-Type": "application/json",
    },
  });

  const data = await res.json();

  return NextResponse.json(data);
}

export async function POST(req: NextApiRequest, res: NextApiResponse) {
  if (req.method == "POST") {
    const { id } = req.query;
    const { body } = req;

    try {
      const response = await fetch(`http://127.0.0.1:8000/authors/${id}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(body), // Convierte el cuerpo de la solicitud a JSON
      });

      const data = await response.json();

      res.status(200).json(data);
    } catch (error) {
      console.error("Error al realizar la solicitud POST:", error);
      res.status(500).json({ error: "Error al realizar la solicitud POST" });
    }
  } else {
    res.status(405).json({ error: 'Método no permitido' });
  }
}
