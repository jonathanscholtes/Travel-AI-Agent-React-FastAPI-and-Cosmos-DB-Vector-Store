import React from 'react'
import {  Box, Stack } from '@mui/material'
import parse from 'html-react-parser'
import './ChatLayout.css'

export default function ChatLayout(messages) {
  return (
    <Stack direction="column" spacing="1">
      {messages.messages.map((obj, i = 0) => (
        <div className="bubbleContainer" key={i}>
          <Box
            key={i++}
            className="bubble"
            sx={{ float: obj.direction, fontSize: '10pt', background: obj.bg }}
          >
            <div>{parse(obj.message)}</div>
          </Box>
        </div>
      ))}
    </Stack>
  )
}
