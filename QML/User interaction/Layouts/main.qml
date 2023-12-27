import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 1.3

Window {
    id:win;
    width: 360
    height: 640
    minimumWidth: 360
    minimumHeight: 640
    visible: true
    title: qsTr("Loyouts")
    Item{
        anchors.fill:parent
        ColumnLayout{
            anchors.fill:parent
            spacing:0

            Line_Bar{
                id: head
                Layout.alignment: Qt.AlignTop
                height: win.height / 9

                Item{
                    width: content.width
                    height: content.height
                    anchors.centerIn: parent
                    RowLayout{
                        anchors.fill:parent
                        spacing:10

                        Backspace{
                        }

                    }


                    Text {
                        id: textHeader
                        text: "header"
                        anchors.centerIn: parent

                    }


                }
            }
            Rectangle {
                id: body
                color: 'gainsboro'
                Layout.fillWidth: true
                Layout.fillHeight: true
                Layout.alignment: Qt.AlignLeft
                Block{
                    width: parent.width * 0.96
                    height: parent.height * 0.96
                    id: content
                    comText: "content"
                }
            }
            Line_Bar{
                id: foot
                anchors.top: body.bottom
                height: win.height / 9

                RowLayout{
                    anchors.fill:parent
                    spacing:10
                    Bt {
                        id: bt_first
                        comText: "1"
                        MouseArea {
                            anchors.fill: bt_first
                            onClicked: {
                                bt_first.comColor="darkgray"
                                bt_first.comColorText="#black"
                                bt_second.comColorText="#666670"
                                bt_third.comColorText="#666670"
                                content.comText="Bt1 clicked"
                                textHeader.text="Bt1 clicked"
                            }

                        }

                    }
                    Bt {
                        id: bt_second
                        comText: "2"
                        MouseArea {
                            anchors.fill: bt_second
                            onClicked: {
                                bt_second.comColor="darkgray"
                                bt_second.comColorText="#black"
                                bt_first.comColorText="#666670"
                                bt_third.comColorText="#666670"
                                content.comText="Bt2 clicked"
                                textHeader.text="Bt2 clicked"
                            }

                        }
                    }
                    Bt {
                        id: bt_third
                        comText: "3"
                        MouseArea {
                            anchors.fill: bt_third
                            onClicked: {
                                bt_third.comColor="darkgray"
                                bt_third.comColorText="#black"
                                bt_first.comColorText="#666670"
                                bt_second.comColorText="#666670"
                                content.comText="Bt3 clicked"
                                textHeader.text="Bt3 clicked"
                            }

                        }
                    }
                }

            }

        }
    }

}
