export default function StatsCard({
  title,
  value
}) {

  return (

    <div className="bg-slate-800 p-6 rounded-2xl shadow-lg">

      <h3 className="text-slate-400 text-sm">
        {title}
      </h3>

      <p className="text-3xl font-bold mt-2">
        {value}
      </p>

    </div>
  );
}
