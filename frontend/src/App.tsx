import React, { ChangeEvent, useState } from 'react';
import { Container, TextField, Button, Accordion, AccordionSummary, AccordionDetails, Typography } from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';


function App() {
  const [textInput, setTextInput] = useState('');

/*
  CHECKPOINT 1
  we need a useEffect here to fetch the latest uploaded video URL
*/

  const handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
    setTextInput(event.target.value);
  };

  const handleSubmit = () => {
    // Perform POST request with textInput data
    console.log('Sending POST request with input:', textInput);
  };

  return (
    <Container>
      <div style={{ marginTop: 20 }}>
        <TextField
          label="Enter text"
          variant="outlined"
          value={textInput}
          onChange={handleInputChange}
          fullWidth
        />
        <Button variant="contained" color="primary" onClick={handleSubmit} style={{ marginTop: 10 }}>
          Submit
        </Button>
      </div>
      <Accordion style={{ marginTop: 20 }}>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography>Video duration and dimensions</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            This is the content for the Video duration and dimensions accordion.
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion style={{ marginTop: 20 }}>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography>Audio Fragment</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            This is the content for the Audio Fragment accordion.
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion style={{ marginTop: 20 }}>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography>Spanish Text Translation</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            This is the content for the Spanish Text Translation accordion.
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion style={{ marginTop: 20 }}>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography>Hear Spanish Translation</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            This is the content for the Hear Spanish Translation accordion.
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion style={{ marginTop: 20 }}>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography>First frame</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            This is the content for the First frame accordion.
          </Typography>
        </AccordionDetails>
      </Accordion>
      <Accordion style={{ marginTop: 20 }}>
        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
          <Typography>Words on First Frame</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>
            This is the content for the Words on First Frame accordion.
          </Typography>
        </AccordionDetails>
      </Accordion>
    </Container>
  );
}

export default App;
