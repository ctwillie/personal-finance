import { AreaChartProps, LineChart } from "@tremor/react";
import { currencyFormatter } from "./value-formatters";

type TransactionAmountByDayProps = {
  data: AreaChartProps["data"];
};

export default function TransactionAmountByDay({
  data,
}: TransactionAmountByDayProps) {
  return (
    <LineChart
      data={data}
      index="date"
      className="h-80"
      categories={["Total Amount"]}
      colors={["teal"]}
      valueFormatter={currencyFormatter}
      yAxisWidth={60}
    />
  );
}
