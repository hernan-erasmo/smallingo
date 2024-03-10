import React, { ChangeEvent, useState, useEffect } from 'react';
import { Container, TextField, Button, Accordion, AccordionSummary, AccordionDetails, Typography } from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import DurationAndDimension from './accordion_components/duration_and_dimensions';
import HearSpanishTranslation from './accordion_components/hear_spanish_translation';
import AudioFragment from './accordion_components/audio_fragment';
import FirstFrame from './accordion_components/first_frame';
import OcrOnFirstFrame from './accordion_components/ocr_on_first_frame';
import SpanishTextTranslation from './accordion_components/spanish_text_translation';


export interface VideoData {
  checkpoint_2: {
    duration: number | null;
    pixels_tall: number | null;
  };
  checkpoint_3: {
    audio_fragment: string | null;
  };
  checkpoint_4: {
    audio_fragment_text: string | null;
  };
  checkpoint_5: {
    audio_fragment_speech: string | null;
  };
  checkpoint_6: {
    video_thumbnail: string | null;
  };
  checkpoint_7: {
    video_ocr: string | null;
  };
}

function App() {
  const [textInput, setTextInput] = useState('');
  const [latestUploadedVideo, setLatestUploadedVideo] = useState('');
  const [submitCount, setSubmitCount] = useState(0);
  const [uploadedVideoId, setUploadedVideoId] = useState('');
  const [videoData, setVideoData] = useState<VideoData | null>(null);

  const accordionData = [
    {
      title: 'Video duration and dimensions',
      content: <DurationAndDimension videoData={videoData} />,
    },
    {
      title: 'Audio Fragment',
      content: <AudioFragment videoData={videoData} />,
    },
    {
      title: 'Spanish Text Translation',
      content: <SpanishTextTranslation />,
    },
    {
      title: 'Hear Spanish Translation',
      content: <HearSpanishTranslation />,
    },
    {
      title: 'First Frame',
      content: <FirstFrame videoData={videoData}/>,
    },
    {
      title: 'OCR on First Frame',
      content: <OcrOnFirstFrame />,
    }
  ];

  useEffect(() => {
  const fetchLatestVideoUrl = async () => {
    try {
      const response = await fetch('http://localhost:8000/videos/latest/');
      if (!response.ok) {
        throw new Error('Failed to fetch latest video URL');
      }
      const data = await response.json();
      setLatestUploadedVideo(data.url);
    } catch (error) {
      console.error('Error fetching latest video URL:', error);
    }
  };
    fetchLatestVideoUrl();
  }, [submitCount]);

  useEffect(() => {
    const fetchLatestVideoUrl = async () => {
      try {
        const response = await fetch('http://localhost:8000/videos/latest/');
        if (!response.ok) {
          throw new Error('Failed to fetch latest video URL');
        }
        const data = await response.json();
        setLatestUploadedVideo(data.url);
      } catch (error) {
        console.error('Error fetching latest video URL:', error);
      }
    };
      fetchLatestVideoUrl();
    }, [submitCount]);

    useEffect(() => {
      const fetchData = async () => {
        try {
          const response = await fetch(`http://localhost:8000/videos/${uploadedVideoId}/`);
          if (!response.ok) {
            throw new Error(`Failed to fetch video data for ID ${uploadedVideoId}`);
          }
          const data: VideoData = await response.json();
          setVideoData(data);
        } catch (error) {
          console.error('Error fetching video data:', error);
        }
      };

      const fetchPeriodically = async () => {
        const endTime = Date.now() + 120 * 1000; // 120 seconds from now
        while (Date.now() < endTime) {
          await fetchData();
          await new Promise(resolve => setTimeout(resolve, 3000)); // Wait for 3 seconds
        }
      };

      if (uploadedVideoId !== null && uploadedVideoId !== '') {
        fetchPeriodically();
      }
    }, [uploadedVideoId]);

  const handleInputChange = (event: ChangeEvent<HTMLInputElement>) => {
    setTextInput(event.target.value);
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch('http://localhost:8000/videos/create/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: textInput }),
      });
      if (!response.ok) {
        console.log("error creating new video: ", response);
        throw new Error('Failed to create new video: ');
      }
      const data = await response.json();
      setUploadedVideoId(data.id); // Store the uploaded video ID
      setSubmitCount(prevCount => prevCount + 1); // Increment submitCount to trigger useEffect
    } catch (error) {
      console.error('Error creating new video:', error);
    }
  };

  return (
    <Container>
      <div style={{ marginTop: 20, display: 'flex', alignItems: 'center', marginBottom: 20}}>
        <TextField
          label="Enter text"
          variant="outlined"
          value={textInput}
          onChange={handleInputChange}
          fullWidth
          style={{ marginRight: 10 }}
        />
        <div style={{ width: 10 }} /> {/* Add gap between TextField and Button */}
        <Button variant="contained" color="primary" onClick={handleSubmit}>
          Submit
        </Button>
      </div>
      <Typography variant="body1">
        Latest uploaded video URL: {
          latestUploadedVideo ?
            latestUploadedVideo :
            'No uploads yet, be the first!'
        }
      </Typography>
      {accordionData.map((item, index) => (
        <Accordion key={index} style={{ marginTop: 20 }}>
          <AccordionSummary expandIcon={<ExpandMoreIcon />}>
            <Typography>{item.title}</Typography>
          </AccordionSummary>
          <AccordionDetails>
            {item.content}
          </AccordionDetails>
        </Accordion>
      ))}
    </Container>
  );
}

export default App;
