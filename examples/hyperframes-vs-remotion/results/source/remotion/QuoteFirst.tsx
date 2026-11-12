import { linearTiming, TransitionSeries } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { slide } from "@remotion/transitions/slide";
import { AbsoluteFill, useVideoConfig } from "remotion";
import {
  ClosingScene,
  GateScene,
  QuoteScene,
  SourceScene,
  TitleScene,
} from "./Scenes";
import { BACKGROUND, TRANSITION_FRAMES } from "./theme";

// Each transition is centred on the brief's cut point (3s, 8s, 13s, 17s),
// so every scene is extended by half a transition per neighbour.
export const QuoteFirst = () => {
  const { fps } = useVideoConfig();

  return (
    <>
      <AbsoluteFill style={{ backgroundColor: BACKGROUND }} />
      <TransitionSeries>
        <TransitionSeries.Sequence
          name="1 Title"
          durationInFrames={3 * fps + TRANSITION_FRAMES / 2}
        >
          <TitleScene />
        </TransitionSeries.Sequence>
        <TransitionSeries.Transition
          presentation={fade()}
          timing={linearTiming({ durationInFrames: TRANSITION_FRAMES })}
        />
        <TransitionSeries.Sequence
          name="2 Open the source"
          durationInFrames={5 * fps + TRANSITION_FRAMES}
        >
          <SourceScene />
        </TransitionSeries.Sequence>
        <TransitionSeries.Transition
          presentation={slide({ direction: "from-right" })}
          timing={linearTiming({ durationInFrames: TRANSITION_FRAMES })}
        />
        <TransitionSeries.Sequence
          name="3 Copy the quote"
          durationInFrames={5 * fps + TRANSITION_FRAMES}
        >
          <QuoteScene />
        </TransitionSeries.Sequence>
        <TransitionSeries.Transition
          presentation={slide({ direction: "from-right" })}
          timing={linearTiming({ durationInFrames: TRANSITION_FRAMES })}
        />
        <TransitionSeries.Sequence
          name="4 The gate"
          durationInFrames={4 * fps + TRANSITION_FRAMES}
        >
          <GateScene />
        </TransitionSeries.Sequence>
        <TransitionSeries.Transition
          presentation={fade()}
          timing={linearTiming({ durationInFrames: TRANSITION_FRAMES })}
        />
        <TransitionSeries.Sequence
          name="5 Closing"
          durationInFrames={3 * fps + TRANSITION_FRAMES / 2}
        >
          <ClosingScene />
        </TransitionSeries.Sequence>
      </TransitionSeries>
    </>
  );
};
