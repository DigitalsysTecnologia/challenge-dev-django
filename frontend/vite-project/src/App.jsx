import React, { useState } from "react";

import CssBaseline from "@mui/material/CssBaseline";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import Error from "./Helper/Error";
import { Button, Input } from "@mui/material";
import useForm from "./Hooks/useForm";
import TableComponent from "./Componets/TableComponent";

function App() {
  const value = useForm();
  const name = useForm();
  const cpf = useForm();
  const address = useForm();
  const [postResult, setPostResult] = useState(null);
  const fortmatResponse = (res) => {
    return JSON.stringify(res, null, 2);
  };

  async function handleSubmit(event) {
    event.preventDefault();
    const formData = {
      value: value.value,
      user: {
        name: name.value,
        cpf: cpf.value,
        address: address.value,
      },
    };

    try {
      const res = await fetch("http://localhost:8000/api/v1/proposals/celery", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });
      console.log(formData);
      console.log(JSON.stringify(formData));
      if (!res.ok) {
        const message = `An error has occured: ${res.status} - ${res.statusText}`;
        throw new Error(message);
      }

      const data = await res.json();

      const result = {
        status: res.status + "-" + res.statusText,
        headers: {
          "Content-Type": res.headers.get("Content-Type"),
          "Content-Length": res.headers.get("Content-Length"),
        },
        data: data,
      };

      setPostResult(fortmatResponse(result));
    } catch (error) {
      setPostResult(error.message);
    }
  }

  return (
    <>
      <CssBaseline />
      <Container maxWidth="xl">
        <Box sx={{ bgcolor: "#cfe8fc", height: "100vh" }}>
          <section>
            <form onSubmit={handleSubmit}>
              <div>
                <div>
                  VALOR:{" "}
                  <Input label="Valor" type="number" name="value" {...value} />
                </div>
                <div>
                  NOME: <Input label="Nome" type="text" name="name" {...name} />
                </div>
                <div>
                  CPF: <Input label="CPF" type="text" name="cpf" {...cpf} />
                </div>
                <div>
                  ENDEREÇO:{" "}
                  <Input
                    label="Endereço"
                    type="text"
                    name="address"
                    {...address}
                  />
                </div>
              </div>

              <Button variant="contained" type="submit">
                Enviar
              </Button>
              {postResult && (
                <div className="alert alert-secondary mt-2" role="alert">
                  <pre>{postResult}</pre>
                </div>
              )}
            </form>
          </section>
          <TableComponent />
        </Box>
      </Container>
    </>
  );
}

export default App;
