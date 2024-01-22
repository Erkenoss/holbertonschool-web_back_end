export default function signUpUser(firstName, lastName) {
  const myPromise = new Promise((resole, reject) => {
    if (firstName && lastName) {
      resole({
        firstName,
        lastName,
      });
    } else {
      reject();
    }
  });
  return myPromise;
}
