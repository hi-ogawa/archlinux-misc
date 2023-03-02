export function difference<T>(lhs: T[], rhs: T[]): T[] {
  const exlucde = new Set(rhs);
  return lhs.filter((x) => !exlucde.has(x));
}
