import React from 'react';
import { VideoData } from '../App';

interface DurationAndDimensionProps {
    videoData: VideoData | null
}

const FirstFrame = (props: DurationAndDimensionProps) => {
    const { videoData } = props;
    const frameSrc = videoData?.checkpoint_6.video_thumbnail;
    const isDisabled = frameSrc ? false : true;
    const baseAddress = "http://localhost:8000"
    const frameHref = baseAddress + frameSrc;
    const downloadButtonLabel = frameSrc ? "Download first frame" : "Loading link, please wait";

    return(
        <div style={ isDisabled ? {pointerEvents: 'none', opacity: 0.5} : {} }>
            <a href={frameSrc ? frameHref : ""} download>{downloadButtonLabel}</a>

            { frameSrc &&
                <img alt="First frame of the uploaded video" src={frameHref}></img>
            }
        </div>
    )
}

export default FirstFrame;
