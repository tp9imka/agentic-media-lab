import type React from "react";
import { AbsoluteFill } from "remotion";
import { AccentBar, Reveal } from "./Reveal";
import { ACCENT, BACKGROUND, MONO, SAFE_X, SAFE_Y, SANS, TEXT } from "./theme";

const frameStyle: React.CSSProperties = {
  backgroundColor: BACKGROUND,
  color: TEXT,
  fontFamily: SANS,
  padding: `${SAFE_Y}px ${SAFE_X}px`,
  justifyContent: "center",
  alignItems: "flex-start",
};

const stepBar: React.CSSProperties = {
  width: 160,
  height: 10,
  backgroundColor: ACCENT,
  transformOrigin: "left center",
  marginBottom: 56,
  flexShrink: 0,
};

const headline: React.CSSProperties = {
  fontSize: 150,
  fontWeight: 700,
  lineHeight: 1.08,
  letterSpacing: "-0.02em",
};

const supporting: React.CSSProperties = {
  fontSize: 78,
  fontWeight: 400,
  lineHeight: 1.25,
};

export const TitleScene = () => (
  <AbsoluteFill style={frameStyle}>
    <Reveal name="Title" delay={0.2} style={{ ...headline, fontSize: 230 }}>
      Quote first<span style={{ color: ACCENT }}>.</span>
    </Reveal>
    <Reveal
      name="Subtitle"
      delay={0.7}
      style={{ ...supporting, marginTop: 40 }}
    >
      How one claim gets into the hub
    </Reveal>
  </AbsoluteFill>
);

export const SourceScene = () => (
  <AbsoluteFill style={frameStyle}>
    <AccentBar name="Step bar" delay={0.15} style={stepBar} />
    <Reveal
      name="Step 1 headline"
      delay={0.3}
      style={{ ...headline, fontSize: 132, whiteSpace: "nowrap" }}
    >
      Open the primary source.
    </Reveal>
    <div style={{ marginTop: 64 }}>
      <Reveal name="Source: skill file" delay={1.2} style={supporting}>
        The skill file.
      </Reveal>
      <Reveal name="Source: licence" delay={1.7} style={supporting}>
        The licence.
      </Reveal>
      <Reveal name="Source: pricing page" delay={2.2} style={supporting}>
        The pricing page.
      </Reveal>
    </div>
  </AbsoluteFill>
);

export const QuoteScene = () => (
  <AbsoluteFill style={frameStyle}>
    <AccentBar name="Step bar" delay={0.15} style={stepBar} />
    <Reveal
      name="Step 2 headline"
      delay={0.3}
      style={{ ...headline, fontSize: 132 }}
    >
      Copy the quote.
      <br />
      Then write the sentence.
    </Reveal>
    <div style={{ display: "flex", marginTop: 72, alignSelf: "stretch" }}>
      <AccentBar
        name="Quote rule"
        delay={1.3}
        collapsed="1 0"
        style={{
          width: 10,
          backgroundColor: ACCENT,
          transformOrigin: "center top",
        }}
      />
      <div style={{ paddingLeft: 48 }}>
        <Reveal
          name="Quote"
          delay={1.4}
          style={{ ...supporting, fontSize: 76, fontStyle: "italic" }}
        >
          Exits are 40-50% shorter than their entrances.
        </Reveal>
        <Reveal
          name="Quote source label"
          delay={2.1}
          style={{ fontSize: 48, marginTop: 28, color: ACCENT }}
        >
          motion.md, section Motion craft
        </Reveal>
      </div>
    </div>
  </AbsoluteFill>
);

export const GateScene = () => (
  <AbsoluteFill style={frameStyle}>
    <AccentBar name="Step bar" delay={0.15} style={stepBar} />
    <Reveal
      name="Step 3 headline"
      delay={0.3}
      style={{ ...headline, fontSize: 120 }}
    >
      The gate finds the quote in the saved source.
    </Reveal>
    <Reveal
      name="Gate output"
      delay={1.4}
      style={{
        fontFamily: MONO,
        fontSize: 70,
        marginTop: 80,
        whiteSpace: "pre",
      }}
    >
      quote-found: <span style={{ color: ACCENT }}>147</span>
      {"   "}quote-not-found: <span style={{ color: ACCENT }}>0</span>
    </Reveal>
  </AbsoluteFill>
);

export const ClosingScene = () => (
  <AbsoluteFill style={frameStyle}>
    <Reveal
      name="Closing line"
      delay={0.4}
      style={{ ...headline, fontSize: 190 }}
    >
      No quote, no claim<span style={{ color: ACCENT }}>.</span>
    </Reveal>
    <Reveal
      name="Project name"
      delay={1}
      style={{ fontSize: 48, marginTop: 56 }}
    >
      agentic-media-lab
    </Reveal>
  </AbsoluteFill>
);
