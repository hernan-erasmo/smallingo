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

    return(
        <div style={ isDisabled ? {pointerEvents: 'none', opacity: 0.5} : {} }>
            <AudioPlayer isDisabled={isDisabled} audioSrc={audioSrc ? audioSrc : ""}/>
            <a href={audioSrc ? audioSrc : ""} download>{downloadButtonLabel}</a>
        </div>
    )
}

export default AudioFragment;
