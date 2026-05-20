import {

  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend

} from "recharts";


export default function ThreatChart({

  history

}) {

  const phishingCount = history.filter(
    item => item.prediction === "phishing"
  ).length;

  const suspiciousCount = history.filter(
    item => item.prediction === "suspicious"
  ).length;

  const safeCount = history.filter(
    item => item.prediction === "safe"
  ).length;


  const data = [

    {
      name: "Phishing",
      value: phishingCount
    },

    {
      name: "Suspicious",
      value: suspiciousCount
    },

    {
      name: "Safe",
      value: safeCount
    }

  ];


  const COLORS = [

    "#ff0000",
    "#facc15",
    "#00ff66"

  ];


  return (

    <div className="bg-slate-800 p-6 rounded-2xl shadow-lg">

      <h2 className="text-2xl font-bold mb-4">
        Threat Analytics
      </h2>

      <PieChart
        width={400}
        height={300}
      >

        <Pie
          data={data}
          cx="50%"
          cy="50%"
          outerRadius={80}
          dataKey="value"
          label
        >

          {data.map((entry, index) => (

            <Cell
              key={`cell-${index}`}
              fill={COLORS[index]}
            />

          ))}

        </Pie>

        <Tooltip />

        <Legend />

      </PieChart>

    </div>

  );

}
