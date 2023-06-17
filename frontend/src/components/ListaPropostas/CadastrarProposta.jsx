import React, { useEffect, useState} from 'react';
import axios from 'axios';
import http from '../http-common';
import { Alert, AlertTitle, Box, Button, Collapse, TextField } from '@mui/material';
import { Navigate } from 'react-router';

const CadastrarProposta = () => {
    const [loading, setLoading] = useState(true);
    const [success, setSuccess] = useState();
    const [redirect, setRedirect] = useState(false)
    const [campos, setCampos] = useState([])
    const [formValues, setFormValues] = useState({
      
    })
    
    
    
    useEffect(() => {
        setLoading(true)
        http.get('/campos')
        .then(response => {
         
          setCampos(response.data)
        })
        
        .then(setLoading(false))
        
        .catch(error =>{
          console.log(error)
          setLoading(false)
        })
        
    }, [loading]);
    const handleInputChange = (e, id) => {
      const { value } = e.target;
      setFormValues({ ...formValues, [id]: value });
      console.log(formValues)
    };
    const handleSubmit = (event) => {
      setLoading(true)
      event.preventDefault();     
      const jsonData = JSON.stringify(formValues);
      http.post('/propostas', jsonData)
      .then(setLoading(false))
      .then(setSuccess(true))
      .then(setTimeout(()=>{
        setRedirect(true)
      }, 3000))
      .catch(erro => console.log(erro))
    };

  if(loading){
    return <p>Carregando..</p>
  }

  if (campos.length === 0) {
    return <p>Não há campos disponíveis para cadastro de propostas</p>
  }
  if(redirect){
    return <Navigate to={'/'}/>
  }
  return (
    
    <div>
     
        <h2>Formulário de proposta</h2>

        
        <Collapse in={success}>
        <Alert severity='success'>
          <AlertTitle>Proposta Cadastrada</AlertTitle>
          Sua proposta será posta na fila para análise. Estamos redirecionando para a lista de propostas
        </Alert>
        </Collapse>

        <Box sx={{maxWidth: '100%'}}>
        <form onSubmit={handleSubmit}>
        {campos.map((i, index)=>(
          
          <div>
            <TextField 
            onChange={(e)=>handleInputChange(e, i.slug)}
            fullWidth 
            label={i.nome} 
            id={i.slug}
            required={i.obrigatorio}
            helperText={i.texto_ajuda}
            margin="normal" />
          </div>
        ))}
        <Button type='submit' variant='contained' color='primary'>
          Enviar proposta
        </Button>
        </form>
        </Box>
      </div>
  )
}

export default CadastrarProposta;