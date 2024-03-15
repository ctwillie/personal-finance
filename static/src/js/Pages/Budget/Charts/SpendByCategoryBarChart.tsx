import React from "react";
import { BarChart } from "@tremor/react";

type SpendByCategoryChartProps = {
  data: Record<string, string>[];
};

/**
 * Data structure example. Array of...
 * {
 *  "category_name": "FOOD_AND_DRINK",
		"spend": 808.90 (number)
 * }
 */
export default function SpendByCategoryChart({
  data,
}: SpendByCategoryChartProps) {
  return (
    <BarChart
      className="overflow-visible"
      showXAxis={false}
      data={React.useMemo(() => data, [])}
      key="spendByCategoryChart"
      index="category_name"
      categories={["spend"]}
      colors={["blue"]}
      yAxisWidth={48}
    />
  );
}
