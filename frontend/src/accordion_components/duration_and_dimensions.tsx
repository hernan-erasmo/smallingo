import React from 'react';
import { VideoData } from '../App';

interface DurationAndDimensionProps {
    videoData: VideoData | null
}

const DurationAndDimension = (props: DurationAndDimensionProps) => {
    const { videoData } = props;
    return(
        <ul>
            <li>Video duration (seconds): {
                videoData?.checkpoint_2.duration ?
                videoData?.checkpoint_2.duration :
                "Loading..."
            }</li>
            <li>Video height (px): {
                videoData?.checkpoint_2.pixels_tall ?
                videoData?.checkpoint_2.pixels_tall :
                "Loading..."
            }</li>
        </ul>
    )
}

export default DurationAndDimension;
