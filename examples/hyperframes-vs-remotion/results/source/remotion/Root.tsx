import { Composition } from "remotion";
import { QuoteFirst } from "./QuoteFirst";

export const RemotionRoot = () => {
  return (
    <>
      <Composition
        id="QuoteFirst"
        component={QuoteFirst}
        durationInFrames={600}
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
