import { ValueFormatter } from "@tremor/react";

const USDollar = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
});

export const currencyFormatter: ValueFormatter = (value: number) => {
  return USDollar.format(value);
};
