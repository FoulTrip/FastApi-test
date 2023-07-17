export default async function Home() {
  const res = await fetch("http://localhost:3000/api");
  const data = await res.json();
  const secondLevelData = data.data
  return (
    <pre>
      {JSON.stringify(
        {
          data: secondLevelData,
        },
        null,
        2
      )}
    </pre>
  );
}
