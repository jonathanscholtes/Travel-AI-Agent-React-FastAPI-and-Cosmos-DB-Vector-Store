import React, { useState } from 'react'
import { Button, Box, Link, Stack, TextField } from '@mui/material'
import SendIcon from '@mui/icons-material/Send'
import './TravelAgent.css'
import {
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
} from '@mui/material'

import ChatLayout from './ChatLayout'

export default function TravelAgent(session) {
  const [open, setOpen] = React.useState(false)
  const [chatPrompt, setChatPrompt] = useState(
    'I want to take a relaxing vacation.',
  )
  const [message, setMessage] = useState([{ 'message': "Hello, how can I assist you today?", 'direction': 'left', 'bg': '#E7FAEC' }])
  const [isLoading, setIsLoading] = useState(false)

  const handlePrompt = (prompt) => {
    setIsLoading(true)
    setChatPrompt('')
    setMessage( message=>[...message, {'message':prompt,'direction':'right', 'bg':'#E7F4FA'}])
    console.log(session.session_id)
    fetch(process.env.REACT_APP_API_HOST + '/agent/' + prompt + "/" + session.session_id)
      .then((response) => response.json())
      .then((res) => {
        setMessage(message => [...message, { 'message': res.text, 'direction': 'left', 'bg': '#E7FAEC' }])
        
        setIsLoading(false)
      })
  }

  const handleClickOpen = () => {
    setOpen(true)
  }

  const handleClose = (value) => {
    setOpen(false)
  }

  return (
    <Box>
      <Dialog onClose={handleClose} open={open} maxWidth="md" fullWidth="true" >
       
        <DialogContent >
          <Stack>
            <Box sx={{ height: '500px' }}>
              <div className="AgentArea">
                
                  <ChatLayout messages={message}/>
                
              </div>
            </Box>
            <Stack direction="row" spacing={0}>
              <TextField
                sx={{ width: '80%' }}
                variant="outlined"
                label="Message"
                helperText="Chat with AI Travel Agent"
                defaultValue="I want to take a relaxing vacation."
                value={chatPrompt}
                onChange={(event) => setChatPrompt(event.target.value)}
              ></TextField>
              <Button
                variant="contained"
                endIcon={<SendIcon />}
                sx={{ mb: 3, ml: 3, mt: 1 }}
                onClick={(event) => handlePrompt(chatPrompt)}
              >
                Submit
              </Button>
            </Stack>
          </Stack>
        </DialogContent>
      </Dialog>
      <Link href="#" onClick={() => handleClickOpen()}>
        <img src={require('.././images/planvoyage.png')} width={'400px'} />
      </Link>
    </Box>
  )
}
