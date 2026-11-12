import type React from "react";
import {
  Easing,
  Interactive,
  interpolate,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

type RevealProps = {
  readonly name: string;
  readonly delay: number;
  readonly children: React.ReactNode;
  readonly style?: React.CSSProperties;
};

export const Reveal = ({ name, delay, children, style }: RevealProps) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  return (
    <Interactive.Div
      name={name}
      style={{
        ...style,
        opacity: interpolate(
          frame,
          [delay * fps, (delay + 0.5) * fps],
          [0, 1],
          {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
            easing: Easing.bezier(0.16, 1, 0.3, 1),
          },
        ),
        translate: interpolate(
          frame,
          [delay * fps, (delay + 0.7) * fps],
          ["0px 56px", "0px 0px"],
          {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
            easing: Easing.bezier(0.16, 1, 0.3, 1),
          },
        ),
      }}
    >
      {children}
    </Interactive.Div>
  );
};

type AccentBarProps = {
  readonly name: string;
  readonly delay: number;
  readonly collapsed?: string;
  readonly style?: React.CSSProperties;
};

export const AccentBar = ({
  name,
  delay,
  collapsed = "0 1",
  style,
}: AccentBarProps) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  return (
    <Interactive.Div
      name={name}
      style={{
        ...style,
        scale: interpolate(
          frame,
          [delay * fps, (delay + 0.6) * fps],
          [collapsed, "1 1"],
          {
            extrapolateLeft: "clamp",
            extrapolateRight: "clamp",
            easing: Easing.bezier(0.16, 1, 0.3, 1),
          },
        ),
      }}
    />
  );
};
