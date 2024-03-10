import React from 'react';
import AudioPlayer from '../components/audio_player';
import { VideoData } from '../App';

interface DurationAndDimensionProps {
    videoData: VideoData | null
}

const AudioFragment = (props: DurationAndDimensionProps) => {
    const { videoData } = props;
    const audioSrc = videoData?.checkpoint_3.audio_fragment;
    const downloadButtonLabel = audioSrc ? "Download audio fragment" : "Loading link, please wait";
    const isDisabled = audioSrc ? false : true;
    const baseAddress = "http://localhost:8000"
    const audioHref = baseAddress + audioSrc;

    return(
        <div style={ isDisabled ? {pointerEvents: 'none', opacity: 0.5} : {} }>
            <AudioPlayer isDisabled={isDisabled} audioSrc={audioSrc ? audioHref : ""}/>
            <a href={audioSrc ? audioHref : ""} download>{downloadButtonLabel}</a>
        </div>
    )
}

export default AudioFragment;
