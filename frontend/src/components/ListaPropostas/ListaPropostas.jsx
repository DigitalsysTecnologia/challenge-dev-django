import React, { useEffect, useState} from 'react';
import axios from 'axios';
import http from '../http-common';
import { TableHead, Table, TableContainer, Paper, TableRow, TableCell } from '@mui/material';


const ListaPropostas = () => {
    const [loading, setLoading] = useState(true);
    const [dados, setDados] = useState([]);
    const hashMap = new Map();
    
    
    useEffect(() => {
        setLoading(true)
        http.get('/propostas')
        .then(response => {
          
          setDados(response.data)
        })
        
        
        .then(setLoading(false))
        .catch(error =>{
          console.log(error)
          setLoading(false)
        })
        
    }, [loading]);
  
  if(loading){
    return <p>Carregando..</p>
  }
  if (dados.length === 0) {
    return <p>Não há Proposta para exibir</p>
  }
  return (
    <div>
        <h2>Lista</h2>
        <TableContainer component={Paper}>
          <Table aria-aria-label='simple table'>
            <TableHead>
              <TableRow>
                <TableCell>#</TableCell>
                <TableCell>Identificação</TableCell>
                <TableCell>Data do registro</TableCell>
                <TableCell>Status</TableCell>
              </TableRow>
            </TableHead>
            {dados.map((i, index)=>(
              <TableRow key={index}>
                  <TableCell>{i.length}</TableCell>
                  <TableCell>{i.__str__}</TableCell>
                  <TableCell>{i.data_registro}</TableCell>
                  <TableCell>{i.status}</TableCell>
                 

              </TableRow>
        ))}
          </Table>
        </TableContainer>
       
        
      </div>
  )
}

export default ListaPropostas;