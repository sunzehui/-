import React, { useEffect, useState } from "react";
import axios from "axios";
export default function GET(props) {
  const { url, params = {}, loading = "", error = "", children } = props;
  const [component, setComponent] = useState(loading());
  useEffect(() => {
    (async () => {
      try {
        const result = await axios.get(url, { params });
        setComponent(children(result.data));
      } catch (err) {
        setComponent(error(err));
      }
    })();
  }, []);
  return component;
}
