import { signUpUser } from './4-user-promise';
import { uploadPhoto } from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.all([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName)
  ])
    .then(([signUpResult, uploadResult]) => {
      return [[{ ...signUpResult }, { ...uploadResult }]];
    })
    .catch((error) => {
      throw error;
    });
}
