import { useState, useEffect } from "react";

import api from "../api/api";

import Navbar from "../components/Navbar";

import ThreatCard from "../components/ThreatCard";

import StatsCard from "../components/StatsCard";

import ThreatChart from "../components/ThreatChart";


export default function Dashboard() {

  const [url, setUrl] = useState("");

  const [result, setResult] = useState(null);

  const [history, setHistory] = useState([]);

  const [loading, setLoading] = useState(false);


  // FETCH HISTORY
  const fetchHistory = async () => {

    try {

      const response = await api.get(
        "/history/"
      );

      setHistory(response.data || []);

    } catch (error) {

      console.error(
        "History fetch failed:",
        error
      );
    }
  };


  useEffect(() => {

    fetchHistory();

  }, []);


  // SCAN URL
  const scanURL = async () => {

    // EMPTY CHECK
    if (!url) {

      alert("Please enter a URL");

      return;
    }

    // URL VALIDATION
    const urlPattern = new RegExp(
      "^(https?:\\/\\/)" +
      "((([a-zA-Z0-9-]+)\\.)+[a-zA-Z]{2,})" +
      "(\\/[a-zA-Z0-9#@%_\\-./?=&]*)?$"
    );

    // INVALID URL CHECK
    if (!urlPattern.test(url)) {

      alert("Enter Correct URL");

      return;
    }

    try {

      setLoading(true);

      const response = await api.post(
        "/scan/",
        {
          url: url,
        }
      );

      setResult(response.data);

      // REFRESH HISTORY
      await fetchHistory();

    } catch (error) {

      console.error(error);

      alert("Error scanning URL");

    } finally {

      setLoading(false);
    }
  };


  // CLEAR HISTORY
  const clearStats = async () => {

    try {

      await api.delete(
        "/history/clear"
      );

      setHistory([]);

      setResult(null);

      setUrl("");

      alert("All stats cleared");

    } catch (error) {

      console.error(error);

      alert("Failed to clear stats");
    }
  };


  // COUNTS
  const phishingCount = history.filter(
    (item) =>
      item.prediction === "phishing"
  ).length;


  const safeCount = history.filter(
    (item) =>
      item.prediction === "safe"
  ).length;


  const suspiciousCount = history.filter(
    (item) =>
      item.prediction === "suspicious"
  ).length;


  // SAFE RATIO
  const safeRatio =
    history.length > 0
      ? `${Math.round(
          (safeCount / history.length) * 100
        )}%`
      : "0%";


  return (

    <div className="min-h-screen bg-slate-900 text-white">

      <Navbar />

      <div className="p-8">

        {/* STATS */}
        <div className="grid md:grid-cols-3 gap-6">

          <StatsCard
            title="Total Scans"
            value={history.length}
          />

          <StatsCard
            title="Threats Detected"
            value={phishingCount}
          />

          <StatsCard
            title="Safe URL Ratio"
            value={safeRatio}
          />

        </div>


        {/* SCANNER + CHART */}
        <div className="grid md:grid-cols-2 gap-6 mt-8">

          {/* URL SCANNER */}
          <div className="bg-slate-800 p-6 rounded-2xl shadow-lg">

            <h2 className="text-2xl font-bold mb-6">
              Scan URL
            </h2>

            <input
              type="text"
              placeholder="Enter suspicious URL..."
              value={url}
              onChange={(e) =>
                setUrl(e.target.value)
              }
              className="w-full p-4 rounded-lg bg-slate-700 text-white placeholder-gray-400"
            />

            <div className="flex gap-4">

              <button
                onClick={scanURL}
                disabled={loading}
                className="mt-4 bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-lg font-bold disabled:opacity-50"
              >
                {loading
                  ? "Scanning..."
                  : "Scan URL"}
              </button>

              <button
                onClick={clearStats}
                className="mt-4 bg-red-600 hover:bg-red-700 px-6 py-3 rounded-lg font-bold"
              >
                Clear Stats
              </button>

            </div>

          </div>


          {/* PIE CHART */}
          <ThreatChart
            history={history}
          />

        </div>


        {/* RESULT */}
        {result && (

          <div className="mt-8">

            <ThreatCard
              result={result}
            />

          </div>

        )}

      </div>

    </div>
  );
}
