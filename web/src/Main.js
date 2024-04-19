import React, { useState, Component } from 'react'
import { Button, Stack, Link, Paper } from '@mui/material'
import { orange } from '@mui/material/colors'
import { styled } from '@mui/material/styles'
import ButtonBase from '@mui/material/ButtonBase'
import TravelAgent from './TripPlanning/TravelAgent'

import './Main.css'

class Main extends Component {
  constructor() {
    super()

    this.state = {
      session_id: ''
    }

    const handleSession = () => {
      
      fetch(process.env.REACT_APP_API_HOST + '/session/')
        .then((response) => response.json())
        .then((res) => {
          this.setState(() => { return { 'session_id': res.session_id } });
          
        })
    }

    if (this.state.session_id ==='') {
      handleSession();
    }

  }

  render() {
    return (
      <div className="Main">
        <div className="Main-Header">
          <Stack direction="row" spacing={5}>
            <img src="/mainlogo.png" alt="Logo" height={'120px'} />
            <Link
              href="#"
              sx={{ color: 'white', fontWeight: 'bold', fontSize: 18 }}
              underline="hover"
            >
              Ships
            </Link>
            <Link
              href="#"
              sx={{ color: 'white', fontWeight: 'bold', fontSize: 18 }}
              underline="hover"
            >
              Destinations
            </Link>
          </Stack>
        </div>
        <div className="Main-Body">
          <div className="Main-Content">
            <Paper elevation={3} sx={{p:1}} >
            <Stack
              direction="row"
              justifyContent="space-evenly"
              alignItems="center"
              spacing={2}
            >
              
                <Link href="#">
                  <img
                    src={require('./images/destinations.png')} width={'400px'} />
                </Link>
                <TravelAgent session_id={this.state.session_id}></TravelAgent>
                <Link href="#">
                  <img
                    src={require('./images/ships.png')} width={'400px'} />
                </Link>
              
              </Stack>
              </Paper>
          </div>
        </div>
        <div className="Main-Footer">
          <b>Disclaimer: Sample Application</b>
          <br />
          Please note that this sample application is provided for demonstration
          purposes only and should not be used in production environments
          without proper validation and testing.
        </div>
      </div>
    )
  }
}

export default Main
