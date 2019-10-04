
function igs(state, slot) {
    var save = {};

    save.t = {};
    save.t.y = state.ty;
    save.t.m = state.ts;
    save.t.d = state.td;
    save.t.w = state.tw;
    save.t.h = state.th;
    save.t.m = state.ty;

    save.p = {};
    save.p.lt = state.pcl;

    save.q = {};
    save.q.f = state.questFlags;

    var saves = JSON.parse(localStorage.getItem("igs"));
    if (!saves) saves = {};
    if (slot) saves[slot] = save;
    else saves.a = save;

    saves = JSON.stringify(saves);
    localStorage.setItem('igs', saves);
}
