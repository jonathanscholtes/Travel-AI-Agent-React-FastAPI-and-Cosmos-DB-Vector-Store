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
import parse from 'html-react-parser';

export default function TravelAgent() {
  const [open, setOpen] = React.useState(false)
  const [chatPrompt, setChatPrompt] = useState(
    'I want to take a relaxing vacation.',
  )
  const [results, setResults] = useState(null)
  const [isLoading, setIsLoading] = useState(false)

  const handlePrompt = () => {
    setIsLoading(true)
    setResults(null)
    fetch(process.env.REACT_APP_API_HOST + '/agent/' + chatPrompt)
      .then((response) => response.json())
      .then((res) => {
        setResults(res)
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
            <Box sx={{ height: '350px' }}>
              <div className="AgentArea">
                <Stack sx={{ p: 2 }}>{
                  results !== null &&
                  results.text}</Stack>
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
                onClick={handlePrompt}
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
