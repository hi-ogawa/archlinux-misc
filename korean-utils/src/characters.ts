import { range } from "@hiogawa/utils";
import { difference } from "./misc";

const OFFSET_CONSONANT = 0x3131;
const OFFSET_VOWEL = 0x314f;
const OFFSET_SYLLABLE = 0xac00;

export const CONSONANTS = range(OFFSET_CONSONANT, OFFSET_CONSONANT + 30).map(
  (i) => String.fromCodePoint(i)
);
export const VOWELS = range(OFFSET_VOWEL, OFFSET_VOWEL + 21).map((i) =>
  String.fromCodePoint(i)
);

export const INITIAL_CONSONANTS = difference(CONSONANTS, [
  "ㄳ",
  "ㄵ",
  "ㄶ",
  "ㄺ",
  "ㄻ",
  "ㄼ",
  "ㄽ",
  "ㄾ",
  "ㄿ",
  "ㅀ",
  "ㅄ",
]);

export const FINAL_CONSONANTS = difference(CONSONANTS, ["ㄸ", "ㅃ", "ㅉ"]);

type SyllableMap = [
  syllable: string,
  initial: string,
  medial: string,
  final: string | undefined
];

export function createSyllableMaps() {
  const result: SyllableMap[] = [];
  let offset = OFFSET_SYLLABLE;
  for (const initial of INITIAL_CONSONANTS) {
    for (const medial of VOWELS) {
      for (const final of [undefined, ...FINAL_CONSONANTS]) {
        result.push([String.fromCodePoint(offset++), initial, medial, final]);
      }
    }
  }
  return result;
}

export const SYLLABLE_MAPS = createSyllableMaps();

export const SYLLABLES = SYLLABLE_MAPS.map((m) => m[0]);
