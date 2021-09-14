import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";

const handleProfileSignup = async (firstName, lastName, fileName) => {
  const ArrayResult = [];
  try {
    const usr = await signUpUser(firstName, lastName);
    ArrayResult.push({ status: 'fulfilled', value: usr });
    await uploadPhoto(fileName);
  } catch (error) {
    ArrayResult.push({
      status: 'rejected',
      value: error.toString(),
    });
  }
  return ArrayResult;
};

export default handleProfileSignup;
