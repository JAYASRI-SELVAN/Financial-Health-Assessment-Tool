import api from "../api";

function Upload() {
  const testBackend = async () => {
    const res = await api.get("/docs");
    console.log(res.status);
  };

  return <button onClick={testBackend}>Test Backend</button>;
}

export default Upload;
