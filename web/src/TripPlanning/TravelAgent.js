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

export default function TravelAgent() {
  const [open, setOpen] = React.useState(false)
  const [chatPrompt, setChatPrompt] = useState(
    'I want to take a vacation with the family',
  )
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
                <Stack sx={{ p: 2 }}>fsdfd</Stack>
              </div>
            </Box>
            <Stack direction="row" spacing={0}>
              <TextField
                sx={{ width: '80%' }}
                variant="outlined"
                label="Message"
                helperText="Chat with AI Travel Agent"
                defaultValue="I want to take a vacation with the family"
                value={chatPrompt}
                onChange={(event) => setChatPrompt(event.target.value)}
              ></TextField>
              <Button
                variant="contained"
                endIcon={<SendIcon />}
                sx={{ mb: 3, ml: 3, mt: 1 }}
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
