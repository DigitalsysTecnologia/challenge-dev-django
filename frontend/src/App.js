import * as React from 'react';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Link from '@mui/material/Link';
import ProTip from './components/ProTip';
import { Collapse, Grid } from '@mui/material';
import { Outlet } from "react-router-dom";
import ResponsiveAppBar from './components/ResponsiveAppBar';


function Copyright() {
  return (
    <Typography variant="body2" color="text.secondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="https://www.linkedin.com/in/niloaires/">
        Nilo Aires jr.
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

export default function App() {
  return (
    <Container maxWidth="lg">
      <ResponsiveAppBar></ResponsiveAppBar>
      <Container>
        <Outlet />
      </Container>
        
      
    
      <Copyright/>
   
    
    </Container>
    
  );
}
