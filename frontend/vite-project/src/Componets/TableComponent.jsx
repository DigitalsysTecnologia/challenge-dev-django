import React from "react";
import { GET } from "../../api";
import { Button } from "@mui/material";
import useFetch from "./../Hooks/useFetch";
import Error from "./../Helper/Error";
import Loading from "./../Helper/Loading";

function TableComponent() {
  const { data, loading, error, request } = useFetch();

  React.useEffect(() => {
    async function loadProposals() {
      const { url, options } = GET();
      const { json } = await request(url, options);
      console.log(json);
    }
    loadProposals();
  }, [request]);

  if (error) return <Error error={error} />;
  if (loading) return <Loading />;
  if (data)
    return (
      <ul>
        <h2>Propostas</h2>
        {data.map((proposal) => (
          <>
            <div>
              {proposal.value} - {proposal.accepted ? "Aceito" : "Recusado"} -{" "}
              {proposal.user.name} - {proposal.user.cpf} -{" "}
              {proposal.user.address}
            </div>
          </>
        ))}
      </ul>
    );
  else return null;
}

export default TableComponent;
