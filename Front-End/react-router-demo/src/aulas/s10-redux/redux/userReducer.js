const initialState = {
    nome: "Ornella"
};

const userReducer = (state = initialState, action) => {

    switch(action.type) {

        case 'CHANGE_NAME':

            return {
                ...state,
                nome: action.payload
            };

        default:
            return state;
    }
};

export default userReducer;
