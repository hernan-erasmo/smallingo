import React, { useState, useRef } from 'react';
import IconButton from '@mui/material/IconButton';
import PlayArrow from '@mui/icons-material/PlayArrow';
import PauseIcon from '@mui/icons-material/Pause';

interface AudioPlayerProps {
    audioSrc: string
    isDisabled: boolean
}

const AudioPlayer = (props: AudioPlayerProps) => {
  const { audioSrc, isDisabled } = props;
  const [isPlaying, setIsPlaying] = useState(false);
  const audioRef = useRef<HTMLAudioElement | null>(null);

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
    <div style={ isDisabled ? {pointerEvents: 'none', opacity: 0.5} : {} }>
      <audio ref={audioRef} src={audioSrc}></audio>
      <IconButton onClick={togglePlay}>
        {isPlaying ? <PauseIcon /> : <PlayArrow />}
      </IconButton>
    </div>
  );
}

export default AudioPlayer;
