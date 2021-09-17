import ClassRoom from './0-classroom';

const initializeRooms = () => {
  const arrayClassRoom = [19, 20, 34];

  return arrayClassRoom.map((n) => new ClassRoom(n));
};

export default initializeRooms;
