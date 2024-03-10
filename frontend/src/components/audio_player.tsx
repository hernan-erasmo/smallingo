import React, { useState, useRef } from 'react';
import IconButton from '@mui/material/IconButton';
import PlayArrow from '@mui/icons-material/PlayArrow';
import PauseIcon from '@mui/icons-material/Pause';

interface AudioPlayerProps {
    audioSrc: string
}

const AudioPlayer = (props: AudioPlayerProps) => {
  const { audioSrc } = props;
  const [isPlaying, setIsPlaying] = useState(false);
  const audioRef = useRef<HTMLAudioElement>(null);

  const togglePlay = () => {
    const audio = audioRef.current;
    if (audio) {
        if (isPlaying) {
            audio.pause();
            } else {
            audio.play();
            }
            setIsPlaying(!isPlaying);
    }
  }

  return (
    <div>
      <audio ref={audioRef} src={audioSrc}></audio>
      <IconButton onClick={togglePlay}>
        {isPlaying ? <PauseIcon /> : <PlayArrow />}
      </IconButton>
    </div>
  );
}

export default AudioPlayer;
