import { AreaChart, AreaChartProps } from "@tremor/react";

type TransactionsByDayProps = {
  data: AreaChartProps["data"];
};

export default function TransactionsByDay({ data }: TransactionsByDayProps) {
  return (
    <AreaChart
      data={data}
      className="h-80"
      index="date"
      categories={["Total Transactions"]}
      colors={["teal"]}
      yAxisWidth={60}
    />
  );
}
