import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([uploadResult, createUserResult]) => {
      console.log(`${uploadResult.body} ${createUserResult.firstName} ${createUserResult.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
