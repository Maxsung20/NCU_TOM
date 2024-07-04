import api from "../axiosAuth";

export const deleteObservation = async (observationIds: number[]) => {
  try {
    const response = await api.delete("/api/observations/delete/", {
      data: { observation_ids: observationIds },
    });
    return response.data;
  } catch (error) {
    console.error("Error deleting observations:", error);
    throw error;
  }
};
