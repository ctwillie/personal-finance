import { BarList, BarListProps } from "@tremor/react";
import { currencyFormatter } from "./value-formatters";

type SpendByCategoryBarListProps = {
  data: BarListProps["data"];
};

export default function SpendByCategoryBarList({
  data,
}: SpendByCategoryBarListProps) {
  return (
    <BarList data={data} color="teal" valueFormatter={currencyFormatter} />
  );
}
