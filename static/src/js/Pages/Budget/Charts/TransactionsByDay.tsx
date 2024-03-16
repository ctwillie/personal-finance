import { AreaChart, AreaChartProps } from "@tremor/react";

type TransactionsByDayProps = {
  data: AreaChartProps["data"];
};

export default function TransactionsByDay({ data }: TransactionsByDayProps) {
  return (
    <AreaChart
      className="h-80"
      data={data}
      index="date"
      categories={["Total Transactions"]}
      colors={["teal"]}
      yAxisWidth={60}
    />
  );
}
