export default function ThreatCard({ result }) {

  const riskColors = {
    HIGH: "bg-red-600",
    MEDIUM: "bg-yellow-500",
    LOW: "bg-green-600",
  };

  return (

    <div className="bg-slate-800 p-6 rounded-2xl mt-8 shadow-lg">

      <div className="flex justify-between items-center">

        <h2 className="text-2xl font-bold">
          Threat Analysis
        </h2>

        <span
          className={`px-4 py-2 rounded-full text-white font-bold ${riskColors[result.risk_score]}`}
        >
          {result.risk_score}
        </span>

      </div>

      <div className="mt-6 space-y-3">

        <p>
          <strong>URL:</strong> {result.url}
        </p>

        <p>
          <strong>Prediction:</strong> {result.prediction}
        </p>

        <p>
          <strong>Confidence:</strong> {result.confidence}%
        </p>

        <p>
          <strong>VirusTotal Malicious:</strong>{" "}
          {result.virustotal?.malicious}
        </p>

        <p>
          <strong>Domain Age:</strong>{" "}
          {result.whois?.domain_age_days} days
        </p>

        <p>
          <strong>SSL Valid:</strong>{" "}
          {result.ssl?.ssl_valid ? "Yes" : "No"}
        </p>

      </div>

    </div>
  );
}
