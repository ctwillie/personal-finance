import React from "react";
import { AxisOptions, Chart } from "react-charts";
import useDemoConfig from "./useDemoConfig";
import ResizableBox from "./ResizableBox";

type DefaultChartProps = {
  //
};

export default function DefaultChart(props: DefaultChartProps) {
  console.log("DefaultChart", props);

  const { data, randomizeData } = useDemoConfig({
    series: 1,
    dataType: "ordinal",
  });

  const primaryAxis = React.useMemo<
    AxisOptions<(typeof data)[number]["data"][number]>
  >(
    () => ({
      getValue: (datum) => datum.primary,
    }),
    []
  );

  const secondaryAxes = React.useMemo<
    AxisOptions<(typeof data)[number]["data"][number]>[]
  >(
    () => [
      {
        getValue: (datum) => datum.secondary,
      },
    ],
    []
  );

  return (
    <>
      <button onClick={randomizeData}>Randomize Data</button>
      <br />
      <br />
      <div className="flex">
        <div>
          <ResizableBox>
            <Chart
              options={{
                data,
                primaryAxis,
                secondaryAxes,
              }}
            />
          </ResizableBox>
        </div>
      </div>
    </>
  );
}
