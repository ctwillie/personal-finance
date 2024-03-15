import { ValueFormatter } from "@tremor/react";

export const currencyFormatter: ValueFormatter = (value: number) => `$${value}`;
