import React, { useState, useEffect } from 'react'
import { Button, Box, Link, Stack, TextField } from '@mui/material'
import SendIcon from '@mui/icons-material/Send'
import { Dialog, DialogContent } from '@mui/material'
import ChatLayout from './ChatLayout'
import './TravelAgent.css'

export default function TravelAgent() {
  const [open, setOpen] = React.useState(false)
  const [session, setSession] = useState('')
  const [chatPrompt, setChatPrompt] = useState(
    'I want to take a relaxing vacation.',
  )
  const [message, setMessage] = useState([
    {
      message: 'Hello, how can I assist you today?',
      direction: 'left',
      bg: '#E7FAEC',
    },
  ])

  const handlePrompt = (prompt) => {
    setChatPrompt('')
    setMessage((message) => [
      ...message,
      { message: prompt, direction: 'right', bg: '#E7F4FA' },
    ])

    fetch(process.env.REACT_APP_API_HOST + '/agent/agent_chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ input: prompt, session_id: session }),
    })
      .then((response) => response.json())
      .then((res) => {
        setMessage((message) => [
          ...message,
          { message: res.text, direction: 'left', bg: '#E7FAEC' },
        ])
      })
  }

  const handleSession = () => {
    fetch(process.env.REACT_APP_API_HOST + '/session/')
      .then((response) => response.json())
      .then((res) => {
        setSession(res.session_id)
      })
  }

  const handleClickOpen = () => {
    setOpen(true)
  }

  const handleClose = (value) => {
    setOpen(false)
  }

  useEffect(() => {
    if (session === '') handleSession()
  }, [])

  return (
    <Box>
      <Dialog onClose={handleClose} open={open} maxWidth="md" fullWidth="true">
        <DialogContent>
          <Stack>
            <Box sx={{ height: '500px' }}>
              <div className="AgentArea">
                <ChatLayout messages={message} />
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
